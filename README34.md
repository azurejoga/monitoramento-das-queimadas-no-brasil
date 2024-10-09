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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14d8af93-5f18-37bd-bcf5-9f49bd4636d7 | -23.8188 | -51.1483 | 2024-10-09 01:22:42 | METOP-B | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 27fb2891-38c5-3c53-bd20-bbb1f6d9bfdc | -23.8221 | -51.161098 | 2024-10-09 01:22:42 | METOP-B | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 67766d5d-cd41-33cb-9b1e-00f6af6b0ca8 | -22.811001 | -48.407799 | 2024-10-09 01:22:46 | METOP-B | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7f904a34-a1ff-38b5-b905-d41f9619866a | -22.796 | -48.391499 | 2024-10-09 01:22:46 | METOP-B | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 87b988d8-69b9-3838-9cfc-5a4c17d171a8 | -22.8015 | -48.4109 | 2024-10-09 01:22:46 | METOP-B | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4fd524a2-550a-3c63-abb4-e3591a6b65dd | -22.791901 | -48.414101 | 2024-10-09 01:22:46 | METOP-B | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0e3c36a5-2e2c-3524-acd9-db4089a31bcc | -22.174601 | -48.111599 | 2024-10-09 01:22:55 | METOP-B | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6b2eed9e-fa3e-31a2-9376-391a8f17ca22 | -22.180401 | -48.132401 | 2024-10-09 01:22:55 | METOP-B | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6fcdf9d6-4683-3626-8427-297091fd12f0 | -22.1863 | -48.153099 | 2024-10-09 01:22:55 | METOP-B | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9ecd2ee3-927a-3aba-ab12-2c290c6cb9d2 | -22.153299 | -48.073002 | 2024-10-09 01:22:55 | METOP-B | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 426ec255-1aaf-30fe-aad5-cd8ae779ac42 | -22.159201 | -48.093899 | 2024-10-09 01:22:55 | METOP-B | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9bae8640-9e30-3076-ae14-92e7318142a9 | -22.1651 | -48.1147 | 2024-10-09 01:22:55 | METOP-B | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 42d82451-73db-3b50-ba77-e84cace83bec | -22.1709 | -48.135399 | 2024-10-09 01:22:55 | METOP-B | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ded41bff-8c0b-35a7-aaf8-9ed3f14d53d6 | -22.176701 | -48.156101 | 2024-10-09 01:22:55 | METOP-B | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8316c3af-2930-3dd1-a8fc-9ec67115aefb | -22.1437 | -48.076099 | 2024-10-09 01:22:55 | METOP-B | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 38ef0ddb-33d4-3bf5-af02-46103450aa25 | -22.149599 | -48.097 | 2024-10-09 01:22:55 | METOP-B | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 005a9bd1-37d3-33a5-8ac6-7fc6caa7d8cd | -22.1555 | -48.117901 | 2024-10-09 01:22:55 | METOP-B | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 88ba7338-9127-389f-902f-587042836cc3 | -22.161301 | -48.138599 | 2024-10-09 01:22:55 | METOP-B | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6e39fe18-aa5b-3b3b-9771-7ee1d48a9edc | -22.167101 | -48.159302 | 2024-10-09 01:22:55 | METOP-B | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 97bd4a4c-0d54-327c-add7-aa11727f3eb6 | -22.134199 | -48.079201 | 2024-10-09 01:22:55 | METOP-B | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f77326f7-6c31-34e1-a5ef-38da54791551 | -22.1401 | -48.100101 | 2024-10-09 01:22:55 | METOP-B | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 78af3131-9f1d-35b5-9274-46e25717c1c3 | -22.145901 | -48.120998 | 2024-10-09 01:22:55 | METOP-B | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 34146e01-ffe0-3af7-a9a6-7c7b761236fa | -22.124599 | -48.082401 | 2024-10-09 01:22:55 | METOP-B | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d5041aba-99ef-3d4e-8ed4-e7988991477f | -22.130501 | -48.103298 | 2024-10-09 01:22:55 | METOP-B | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 57e3158d-3f86-381b-bff0-c04006e745ef | -22.115101 | -48.085499 | 2024-10-09 01:22:56 | METOP-B | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f361c5ae-bf53-3726-8433-75d0af6d7ad9 | -22.121 | -48.1064 | 2024-10-09 01:22:56 | METOP-B | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c7d578a3-549a-3aa6-a50d-fcef42a91e61 | -22.105499 | -48.0886 | 2024-10-09 01:22:56 | METOP-B | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b38125cc-1872-3e1c-b9d9-f59f32ca4159 | -21.5574 | -46.9384 | 2024-10-09 01:22:59 | METOP-B | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d2b695ff-d62d-3823-938b-d0e47cdf6504 | -21.564699 | -46.963699 | 2024-10-09 01:22:59 | METOP-B | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7e469963-2626-3011-8d40-34293000f03c | -21.547899 | -46.9417 | 2024-10-09 01:22:59 | METOP-B | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| cd4a8545-e2c0-394c-97c4-b8e59a5fc078 | -21.555201 | -46.9669 | 2024-10-09 01:22:59 | METOP-B | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| fb3421b8-7985-38ce-8326-38b7cbcac2cf | -21.538401 | -46.944801 | 2024-10-09 01:23:00 | METOP-B | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8f165123-1b0f-38f6-b420-d703ee3a9c1d | -23.337601 | -53.891998 | 2024-10-09 01:23:00 | METOP-B | ITAQUIRAÍ | MATO GROSSO DO SUL | Brasil | 5004601 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 46ce01b1-b001-37f2-9888-e97e6e1598e0 | -21.623301 | -47.676102 | 2024-10-09 01:23:02 | METOP-B | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c9995cbf-81c5-3571-ac32-43dea2d8ec43 | -21.6073 | -47.656502 | 2024-10-09 01:23:02 | METOP-B | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c3307b88-2787-384b-ac62-e543bf5e77b4 | -21.6138 | -47.679199 | 2024-10-09 01:23:02 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 491e4940-37ac-3164-a91c-d14b50aa48de | -21.591299 | -47.636902 | 2024-10-09 01:23:02 | METOP-B | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ab23519a-e548-32bd-aa1a-5fcd1c38d781 | -21.597799 | -47.659698 | 2024-10-09 01:23:02 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9308033b-ea12-3425-a6b1-54120ced0863 | -21.6043 | -47.6824 | 2024-10-09 01:23:02 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7c5abe58-0d4f-3cfd-8604-409f012a6aee | -21.610701 | -47.705002 | 2024-10-09 01:23:02 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b5f8e847-311e-30a7-be59-44419f93722a | -21.581699 | -47.639999 | 2024-10-09 01:23:02 | METOP-B | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9adfc635-d94a-39b4-b4cc-acd22e3b8ffa | -21.5882 | -47.6628 | 2024-10-09 01:23:02 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d87c64cd-999e-3051-a1d9-3ea51f66031e | -21.5947 | -47.685501 | 2024-10-09 01:23:02 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2db2439c-5487-33ac-b7a1-1c43f5b095f2 | -21.601101 | -47.708099 | 2024-10-09 01:23:02 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5707d6c4-62f9-3cc6-bc5f-0b16748e72b7 | -21.578699 | -47.666 | 2024-10-09 01:23:02 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2c33507f-4f6f-3fb2-9132-26296a743ff9 | -21.585199 | -47.688702 | 2024-10-09 01:23:02 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1bb42e56-b1c0-34bc-acbb-67ef9c457d94 | -21.556601 | -47.845001 | 2024-10-09 01:23:03 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| aae55927-d1f4-3dc9-b34b-29b5c876d717 | -21.562799 | -47.8671 | 2024-10-09 01:23:03 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| fa8d6e3d-4814-3f9f-870f-0ec3e72f5a11 | -21.8134 | -49.139099 | 2024-10-09 01:23:05 | METOP-B | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e497834d-025b-31df-84be-b9e1103bf003 | -21.818399 | -49.157299 | 2024-10-09 01:23:05 | METOP-B | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 629ba95b-a3e4-3a3f-ac5d-1c72aacb7d07 | -21.803801 | -49.142101 | 2024-10-09 01:23:05 | METOP-B | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d9b38003-8d81-30d1-b88e-57907604cc66 | -21.0914 | -47.203499 | 2024-10-09 01:23:08 | METOP-B | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5ca7fb1c-a314-3fed-807b-e75428045c63 | -21.0819 | -47.206699 | 2024-10-09 01:23:08 | METOP-B | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 67f3b955-ceb7-346c-bd14-310bf19f006c | -20.6308 | -45.8452 | 2024-10-09 01:23:09 | METOP-B | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d03ef028-4222-3302-8f2b-65aa89d3357f | -20.639999 | -45.875801 | 2024-10-09 01:23:09 | METOP-B | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c0a1ab29-ad86-33e0-b1b5-6592e7961a92 | -20.621099 | -45.882301 | 2024-10-09 01:23:09 | METOP-B | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| eab22bd7-162b-3aae-b450-3198ff328f74 | -20.611601 | -45.885502 | 2024-10-09 01:23:09 | METOP-B | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 10915e9a-07a6-3c04-a215-07448eb5d368 | -20.779301 | -47.169701 | 2024-10-09 01:23:13 | METOP-B | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 08bcb9ce-0ded-336b-b682-2efdde003250 | -20.7698 | -47.172798 | 2024-10-09 01:23:13 | METOP-B | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a0d0c4d8-40e5-359f-affc-25506b77ba8d | -20.7675 | -47.201199 | 2024-10-09 01:23:13 | METOP-B | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 063fd587-9e4f-390d-bb7a-d131502a9590 | -20.7747 | -47.226299 | 2024-10-09 01:23:13 | METOP-B | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 365ac413-37cb-3f36-a935-62f96ef92b6d | -20.757999 | -47.2043 | 2024-10-09 01:23:13 | METOP-B | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c100074f-f98c-3064-9212-6759776ed9fb | -20.7652 | -47.229401 | 2024-10-09 01:23:13 | METOP-B | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 324aaa0e-bb62-3399-86e9-6018f3770424 | -20.7724 | -47.254398 | 2024-10-09 01:23:13 | METOP-B | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 936fae8e-2fd8-36b5-bfb1-16b2d2de9bdd | -20.748501 | -47.207401 | 2024-10-09 01:23:13 | METOP-B | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 04f54ceb-005d-3883-97ed-d81fd090bb5a | -20.755699 | -47.232498 | 2024-10-09 01:23:13 | METOP-B | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c95134cd-ed80-3aa9-8647-85455e6c31df | -20.4389 | -48.8032 | 2024-10-09 01:23:26 | METOP-B | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 480db88f-4806-3aa0-be4a-637fee987237 | -20.400499 | -48.815201 | 2024-10-09 01:23:26 | METOP-B | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 57736a82-771f-3c07-aabf-215e80f37a48 | -20.351299 | -48.6754 | 2024-10-09 01:23:26 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2502d9a3-51e0-33d7-958b-d550b2dd97b9 | -20.357 | -48.695999 | 2024-10-09 01:23:26 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| cfe48a53-e1c1-362f-a808-79a523bf9ada | -20.3909 | -48.818199 | 2024-10-09 01:23:26 | METOP-B | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5ac0c062-f3ef-370e-b77f-452ded0cce27 | -20.3417 | -48.678501 | 2024-10-09 01:23:27 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f3a84a5c-f8fb-3f4a-a528-7ba5d4c80f77 | -20.3475 | -48.6991 | 2024-10-09 01:23:27 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 392d546b-d4f5-3430-8947-d1eb4f982040 | -20.353201 | -48.719601 | 2024-10-09 01:23:27 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 473e01ce-312d-3855-b5ab-928f8bb19bba | -20.3321 | -48.681499 | 2024-10-09 01:23:27 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b7f69976-534f-37fc-aa7c-04453d19f9ca | -20.3379 | -48.702099 | 2024-10-09 01:23:27 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c813a1c7-c2c5-3009-9ac8-e7fcbcd47cce | -20.343599 | -48.722599 | 2024-10-09 01:23:27 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 73947ffa-0706-3c70-af73-0943c3eb7921 | -20.3225 | -48.684502 | 2024-10-09 01:23:27 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a4c201ab-db22-3f82-9993-fa0bed3995ad | -20.3283 | -48.705101 | 2024-10-09 01:23:27 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b1b0353f-694e-35ce-b7d2-3aa835ef58d1 | -20.334 | -48.725601 | 2024-10-09 01:23:27 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e2a3af31-0185-39c6-9ec4-ca35efa8a3ad | -20.345301 | -48.766499 | 2024-10-09 01:23:27 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3f024164-9075-3f78-a80c-d66e37731181 | -20.313 | -48.6875 | 2024-10-09 01:23:27 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 673e7198-47f4-306a-9532-60abd761594b | -20.318701 | -48.708099 | 2024-10-09 01:23:27 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3f3f69ba-a49f-371a-8952-b28b122bef26 | -20.3239 | -48.839298 | 2024-10-09 01:23:28 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 56d11fb2-404c-3dd9-beb9-f2bca53acb05 | -20.5525 | -50.097099 | 2024-10-09 01:23:29 | METOP-B | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3d541f42-d428-3deb-b286-7163ca2fef35 | -20.542801 | -50.100101 | 2024-10-09 01:23:30 | METOP-B | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9a5104e6-714b-3e8f-9549-afcb6f74bfc5 | -20.533199 | -50.103001 | 2024-10-09 01:23:30 | METOP-B | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6a63297f-029d-3736-8109-c95933c7fef8 | -21.652901 | -54.4757 | 2024-10-09 01:23:30 | METOP-B | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9bc354c3-2651-3f5c-ac65-2c0ac4815a77 | -20.100201 | -48.821301 | 2024-10-09 01:23:31 | METOP-B | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 136dcd54-868d-3f1c-bf27-473b19dc5188 | -20.1042 | -48.797901 | 2024-10-09 01:23:31 | METOP-B | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| decfac61-e8d2-33aa-975c-9332dbb90b1f | -20.0889 | -48.780399 | 2024-10-09 01:23:31 | METOP-B | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 66aaa9cc-057e-3ad6-ad45-57e749f5b51e | -20.094601 | -48.8009 | 2024-10-09 01:23:31 | METOP-B | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1a5f4c59-e49a-3b9c-ad8b-93f861ed5b16 | -20.084999 | -48.803902 | 2024-10-09 01:23:31 | METOP-B | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2cbc4e24-b12a-3dc9-a216-288893551fa4 | -21.9034 | -56.445301 | 2024-10-09 01:23:33 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ef5c8251-b5cb-3d0d-b5e4-4b3f37ddc5ce | -21.350201 | -54.5965 | 2024-10-09 01:23:35 | METOP-B | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| bbf1b2dd-ccce-3194-ab0a-dbc334ee72e4 | -21.385401 | -55.671398 | 2024-10-09 01:23:38 | METOP-B | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9252c409-0676-3efe-b28d-2631c544d788 | -21.3873 | -55.679501 | 2024-10-09 01:23:38 | METOP-B | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 93d4360c-224f-37d2-b99a-9b139e91737e | -20.888901 | -54.9655 | 2024-10-09 01:23:44 | METOP-B | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 36fd025f-2c1c-33ce-9dca-13b2c9647bdc | -20.268801 | -56.5233 | 2024-10-09 01:24:00 | METOP-B | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b12ed297-26bf-3969-8d3d-44b905c1f88d | -20.103001 | -55.938301 | 2024-10-09 01:24:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README35.md)
